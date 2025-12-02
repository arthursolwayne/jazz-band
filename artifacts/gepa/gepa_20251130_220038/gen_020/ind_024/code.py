
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (37, 1.5, 0.375), (38, 1.875, 0.375), (36, 2.25, 0.375), (35, 2.625, 0.375),
    (37, 3.0, 0.375), (38, 3.375, 0.375), (36, 3.75, 0.375), (35, 4.125, 0.375),
    (37, 4.5, 0.375), (38, 4.875, 0.375), (36, 5.25, 0.375), (35, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (64, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375), (71, 1.875, 0.375),
    # Bar 3: F7 on beat 2
    (64, 3.375, 0.375), (67, 3.375, 0.375), (69, 3.375, 0.375), (71, 3.375, 0.375),
    # Bar 4: F7 on beat 2
    (64, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375), (71, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_start = bar_start
    snare_start = bar_start + 0.375
    hihat_start = bar_start
    kick_end = kick_start + 0.375
    snare_end = snare_start + 0.375
    hihat_end = hihat_start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    for i in range(8):
        hihat_note_start = hihat_start + i * 0.1875
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_note_start, end=hihat_note_start + 0.1875))

# Sax (Dante): Motif in F, start on beat 2 of bar 2
# F - G - A - Bb (saxophone transposes, so play in Bb)
# Motif: Bb - A - G - F
# Bb = 48, A = 47, G = 46, F = 45
sax_notes = [
    (48, 1.875, 0.375), (47, 2.25, 0.375), (46, 2.625, 0.375), (45, 3.0, 0.375),
    (48, 3.375, 0.375), (47, 3.75, 0.375), (46, 4.125, 0.375), (45, 4.5, 0.375),
    (48, 4.875, 0.375), (47, 5.25, 0.375), (46, 5.625, 0.375), (45, 6.0, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
