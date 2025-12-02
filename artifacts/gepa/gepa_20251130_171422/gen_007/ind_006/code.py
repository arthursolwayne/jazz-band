
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
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (53, 1.5, 0.375),  # D
    (52, 1.875, 0.375), # C
    (54, 2.25, 0.375),  # Eb
    (55, 2.625, 0.375), # F
    # Bar 3
    (56, 3.0, 0.375),   # G
    (55, 3.375, 0.375), # F
    (54, 3.75, 0.375),  # Eb
    (53, 4.125, 0.375), # D
    # Bar 4
    (52, 4.5, 0.375),   # C
    (53, 4.875, 0.375), # D
    (55, 5.25, 0.375),  # F
    (57, 5.625, 0.375)  # G
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875, 0.375),  # C7 (C, E, Bb)
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    # Bar 3
    (62, 3.375, 0.375),  # D7 (D, F#, C)
    (65, 3.375, 0.375),
    (69, 3.375, 0.375),
    # Bar 4
    (60, 4.875, 0.375),  # C7 again
    (64, 4.875, 0.375),
    (67, 4.875, 0.375)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    drum_notes.append((36, start + 0.0, 0.375))
    drum_notes.append((36, start + 0.75, 0.375))
    # Snare on 2 and 4
    drum_notes.append((38, start + 0.375, 0.375))
    drum_notes.append((38, start + 1.125, 0.375))
    # Hihat on every eighth
    for i in range(4):
        drum_notes.append((42, start + i * 0.375, 0.375))

for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Sax (Dante) - Motif
# Bar 2: Start motif
sax_notes = [
    (62, 1.5, 0.375),  # E (F7)
    (64, 1.875, 0.375), # G
    (62, 2.25, 0.375),  # E
    (60, 2.625, 0.375), # D (hang)
    # Bar 3: Come back with variation
    (62, 3.0, 0.375),   # E
    (64, 3.375, 0.375), # G
    (62, 3.75, 0.375),  # E
    (61, 4.125, 0.375), # Eb
    # Bar 4: Finish motif
    (62, 4.5, 0.375),   # E
    (64, 4.875, 0.375), # G
    (62, 5.25, 0.375),  # E
    (60, 5.625, 0.375)  # D
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
