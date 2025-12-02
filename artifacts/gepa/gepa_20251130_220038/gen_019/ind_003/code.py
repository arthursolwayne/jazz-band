
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5, 0.375),   # D (root)
    (61, 1.875, 0.375), # C# (chromatic approach)
    (63, 2.25, 0.375),  # Eb (3rd)
    (62, 2.625, 0.375), # D (root)
    (64, 2.625, 0.375), # F (5th)
    (63, 3.0, 0.375),   # Eb (3rd)
    (62, 3.375, 0.375), # D (root)
    (61, 3.75, 0.375),  # C# (chromatic approach)
    (62, 4.125, 0.375), # D (root)
    (63, 4.5, 0.375),   # Eb (3rd)
    (62, 4.875, 0.375), # D (root)
    (64, 5.25, 0.375),  # F (5th)
    (63, 5.625, 0.375), # Eb (3rd)
    (62, 6.0, 0.375)    # D (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 0.1875),  # D7 (D, F#, A, C)
    (69, 1.5, 0.1875),
    (71, 1.5, 0.1875),
    (67, 1.5, 0.1875),
    (69, 1.875, 0.1875), # 2nd beat
    (71, 1.875, 0.1875),
    (67, 1.875, 0.1875),
    (64, 1.875, 0.1875),
    # Bar 3
    (64, 2.25, 0.1875),
    (69, 2.25, 0.1875),
    (71, 2.25, 0.1875),
    (67, 2.25, 0.1875),
    (69, 2.625, 0.1875),
    (71, 2.625, 0.1875),
    (67, 2.625, 0.1875),
    (64, 2.625, 0.1875),
    # Bar 4
    (64, 3.0, 0.1875),
    (69, 3.0, 0.1875),
    (71, 3.0, 0.1875),
    (67, 3.0, 0.1875),
    (69, 3.375, 0.1875),
    (71, 3.375, 0.1875),
    (67, 3.375, 0.1875),
    (64, 3.375, 0.1875),
    (69, 3.75, 0.1875),
    (71, 3.75, 0.1875),
    (67, 3.75, 0.1875),
    (64, 3.75, 0.1875),
    (69, 4.125, 0.1875),
    (71, 4.125, 0.1875),
    (67, 4.125, 0.1875),
    (64, 4.125, 0.1875),
    (69, 4.5, 0.1875),
    (71, 4.5, 0.1875),
    (67, 4.5, 0.1875),
    (64, 4.5, 0.1875),
    (69, 4.875, 0.1875),
    (71, 4.875, 0.1875),
    (67, 4.875, 0.1875),
    (64, 4.875, 0.1875),
    (69, 5.25, 0.1875),
    (71, 5.25, 0.1875),
    (67, 5.25, 0.1875),
    (64, 5.25, 0.1875),
    (69, 5.625, 0.1875),
    (71, 5.625, 0.1875),
    (67, 5.625, 0.1875),
    (64, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375), # F
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # Bb
    (62, 3.0, 0.375),   # D (come back)
    (64, 3.375, 0.375), # F
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # Bb
    (62, 4.5, 0.375),   # D (finish it)
    (64, 4.875, 0.375), # F
    (62, 5.25, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Fill the bar
# Bar 2
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
