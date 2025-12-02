
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 1.0),      # Kick on 1
    (42, 0.0, 1.0),      # Hihat on 1
    (38, 0.5, 1.0),      # Snare on 2
    (42, 0.5, 1.0),      # Hihat on 2
    (36, 1.0, 1.0),      # Kick on 3
    (42, 1.0, 1.0),      # Hihat on 3
    (38, 1.5, 1.0),      # Snare on 4
    (42, 1.5, 1.0),      # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),   # D (1)
    (63, 1.875, 0.375), # Eb (2)
    (64, 2.25, 0.375),  # E (3)
    (65, 2.625, 0.375), # F (4)
    (67, 3.0, 0.375),   # G (1)
    (68, 3.375, 0.375), # Ab (2)
    (69, 3.75, 0.375),  # A (3)
    (70, 4.125, 0.375), # Bb (4)
    (72, 4.5, 0.375),   # B (1)
    (73, 4.875, 0.375), # C (2)
    (74, 5.25, 0.375),  # C# (3)
    (76, 5.625, 0.375), # D (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.5, 0.375),   # G7 (1)
    (71, 1.875, 0.375), # Bb (2)
    (74, 1.875, 0.375), # C# (2)
    (62, 2.25, 0.375),  # D (3)
    (67, 2.625, 0.375), # G7 (4)
    (71, 2.625, 0.375), # Bb (4)
    (74, 2.625, 0.375), # C# (4)
    # Bar 3
    (72, 3.0, 0.375),   # B7 (1)
    (76, 3.375, 0.375), # D (2)
    (79, 3.375, 0.375), # F# (2)
    (72, 3.75, 0.375),  # B7 (3)
    (76, 4.125, 0.375), # D (4)
    (79, 4.125, 0.375), # F# (4)
    # Bar 4
    (67, 4.5, 0.375),   # G7 (1)
    (71, 4.875, 0.375), # Bb (2)
    (74, 4.875, 0.375), # C# (2)
    (62, 5.25, 0.375),  # D (3)
    (67, 5.625, 0.375), # G7 (4)
    (71, 5.625, 0.375), # Bb (4)
    (74, 5.625, 0.375), # C# (4)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (67, 1.5, 0.375),   # G (1)
    (71, 1.875, 0.375), # Bb (2)
    (74, 2.25, 0.375),  # C# (3)
    (67, 2.625, 0.375), # G (4)
    (67, 3.0, 0.375),   # G (1)
    (71, 3.375, 0.375), # Bb (2)
    (74, 3.75, 0.375),  # C# (3)
    (67, 4.125, 0.375), # G (4)
    (67, 4.5, 0.375),   # G (1)
    (71, 4.875, 0.375), # Bb (2)
    (74, 5.25, 0.375),  # C# (3)
    (67, 5.625, 0.375), # G (4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Bar 2
    if bar == 2:
        kick = (36, start, 1.0)
        snare = (38, start + 0.5, 1.0)
    else:
        kick = (36, start, 1.0)
        snare = (38, start + 0.5, 1.0)
    hihat = (42, start, 1.0)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick[0], start=kick[1], end=kick[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare[0], start=snare[1], end=snare[2]))
    for i in range(0, 4):
        hihat_notes = (42, start + i * 0.375, 0.375)
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_notes[0], start=hihat_notes[1], end=hihat_notes[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
