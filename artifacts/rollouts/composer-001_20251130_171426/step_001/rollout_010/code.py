
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums - Bar 1 (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on beat 1
    (38, 0.75, 0.375), # Snare on beat 2
    (42, 0.0, 0.1875), # Hihat on 1& (0.0)
    (42, 0.1875, 0.1875), # Hihat on 1&
    (42, 0.375, 0.1875), # Hihat on 2&
    (42, 0.5625, 0.1875), # Hihat on 3&
    (42, 0.75, 0.1875), # Hihat on 2&
    (42, 0.9375, 0.1875), # Hihat on 3&
    (42, 1.125, 0.1875), # Hihat on 4&
    (36, 1.125, 0.375)  # Kick on beat 3
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4 (1.5 - 6.0s)

# Bass line (Marcus) - Walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb (chromatic)
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375), # F
    (62, 2.625, 0.375),  # D (beat 1 of bar 2)
    (63, 3.0, 0.375),   # Eb (chromatic)
    (64, 3.375, 0.375), # E
    (65, 3.75, 0.375),  # F
    (62, 3.75, 0.375),  # D (beat 1 of bar 3)
    (63, 4.125, 0.375), # Eb (chromatic)
    (64, 4.5, 0.375),   # E
    (65, 4.875, 0.375), # F
    (62, 4.875, 0.375),  # D (beat 1 of bar 4)
    (63, 5.25, 0.375),  # Eb (chromatic)
    (64, 5.625, 0.375), # E
    (65, 6.0, 0.375)    # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (64, 2.25, 0.375),  # D7 (D, F#, A, C)
    (69, 2.25, 0.375),
    (76, 2.25, 0.375),
    (71, 2.25, 0.375),
    (62, 2.625, 0.375),  # D7 on beat 4
    (67, 2.625, 0.375),
    (74, 2.625, 0.375),
    (69, 2.625, 0.375),
    # Bar 3
    (64, 3.375, 0.375),  # D7
    (69, 3.375, 0.375),
    (76, 3.375, 0.375),
    (71, 3.375, 0.375),
    (62, 3.75, 0.375),   # D7 on beat 4
    (67, 3.75, 0.375),
    (74, 3.75, 0.375),
    (69, 3.75, 0.375),
    # Bar 4
    (64, 4.5, 0.375),    # D7
    (69, 4.5, 0.375),
    (76, 4.5, 0.375),
    (71, 4.5, 0.375),
    (62, 4.875, 0.375),  # D7 on beat 4
    (67, 4.875, 0.375),
    (74, 4.875, 0.375),
    (69, 4.875, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Drums (Little Ray) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax (Dante) - Motif starts on bar 2, plays a short phrase, leaves it hanging
sax_notes = [
    # Bar 2
    (69, 2.25, 0.375),  # E
    (71, 2.625, 0.375), # F
    # Bar 3
    (67, 3.375, 0.375),  # D
    (69, 3.75, 0.375),   # E
    # Bar 4
    (64, 4.5, 0.375),    # D
    (69, 4.875, 0.375)   # E
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
