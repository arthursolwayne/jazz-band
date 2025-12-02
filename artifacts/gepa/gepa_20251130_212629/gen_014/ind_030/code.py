
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
    # Bar 1
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &
    (36, 1.5, 0.375),   # Kick on 3
    (38, 1.5, 0.375),   # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# D Dorian mode: D, E, F#, G, A, B, C
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375),  # D
    (60, 1.875, 0.375), # F# (chromatic approach)
    (62, 2.25, 0.375),  # D
    (64, 2.625, 0.375), # F# (chromatic approach)
    # Bar 3 (3.0 - 4.5s)
    (65, 3.0, 0.375),  # G
    (63, 3.375, 0.375), # E (chromatic approach)
    (65, 3.75, 0.375),  # G
    (67, 4.125, 0.375), # B (chromatic approach)
    # Bar 4 (4.5 - 6.0s)
    (67, 4.5, 0.375),  # B
    (65, 4.875, 0.375), # G (chromatic approach)
    (67, 5.25, 0.375),  # B
    (64, 5.625, 0.375), # F# (chromatic approach)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
# D7 = D, F#, A, C
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 2.25, 0.375),  # D7 on beat 3
    (65, 2.625, 0.375), # A
    (60, 2.625, 0.375), # F#
    (64, 2.625, 0.375), # C
    # Bar 3 (3.0 - 4.5s)
    (62, 4.5, 0.375),   # D7 on beat 4
    (65, 4.875, 0.375), # A
    (60, 4.875, 0.375), # F#
    (64, 4.875, 0.375), # C
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D to F# to A, then return to D later
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375),   # D
    (66, 1.875, 0.375),  # F#
    (69, 2.25, 0.375),   # A
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.375),   # D
    (66, 3.375, 0.375),  # F#
    (69, 3.75, 0.375),   # A
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375),   # D
    (66, 4.875, 0.375),  # F#
    (69, 5.25, 0.375),   # A
    (69, 5.625, 0.375),  # A
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
