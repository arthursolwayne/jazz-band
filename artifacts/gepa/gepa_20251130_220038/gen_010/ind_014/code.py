
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1& 
    (42, 0.1875, 0.1875),# Hihat on 2
    (38, 0.375, 0.375),  # Snare on 3
    (42, 0.375, 0.1875), # Hihat on 3&
    (42, 0.5625, 0.1875),# Hihat on 4
    (36, 0.75, 0.375),   # Kick on 2
    (42, 0.75, 0.1875),  # Hihat on 2&
    (42, 0.9375, 0.1875),# Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4&
    (42, 1.3125, 0.1875) # Hihat on 1
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line in Fm, chromatic approaches
bass_notes = [
    (48, 1.5, 0.375), # F
    (50, 1.875, 0.375),# Gb
    (48, 2.25, 0.375), # F
    (46, 2.625, 0.375),# Eb
    (48, 3.0, 0.375),  # F
    (50, 3.375, 0.375),# Gb
    (48, 3.75, 0.375), # F
    (46, 4.125, 0.375),# Eb
    (45, 4.5, 0.375),  # D
    (48, 4.875, 0.375),# F
    (50, 5.25, 0.375), # Gb
    (48, 5.625, 0.375) # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.5, 0.1875), # F7 on 1
    (57, 1.5, 0.1875),
    (59, 1.5, 0.1875),
    (52, 1.5, 0.1875),
    (50, 1.875, 0.1875), # comp on 2
    (57, 1.875, 0.1875),
    (52, 1.875, 0.1875),
    (50, 2.25, 0.1875), # F7 on 3
    (57, 2.25, 0.1875),
    (59, 2.25, 0.1875),
    (52, 2.25, 0.1875),
    (50, 2.625, 0.1875), # comp on 4
    (57, 2.625, 0.1875),
    (52, 2.625, 0.1875),
    (50, 3.0, 0.1875), # F7 on 1
    (57, 3.0, 0.1875),
    (59, 3.0, 0.1875),
    (52, 3.0, 0.1875),
    (50, 3.375, 0.1875), # comp on 2
    (57, 3.375, 0.1875),
    (52, 3.375, 0.1875),
    (50, 3.75, 0.1875), # F7 on 3
    (57, 3.75, 0.1875),
    (59, 3.75, 0.1875),
    (52, 3.75, 0.1875),
    (50, 4.125, 0.1875), # comp on 4
    (57, 4.125, 0.1875),
    (52, 4.125, 0.1875),
    (50, 4.5, 0.1875), # F7 on 1
    (57, 4.5, 0.1875),
    (59, 4.5, 0.1875),
    (52, 4.5, 0.1875),
    (50, 4.875, 0.1875), # comp on 2
    (57, 4.875, 0.1875),
    (52, 4.875, 0.1875),
    (50, 5.25, 0.1875), # F7 on 3
    (57, 5.25, 0.1875),
    (59, 5.25, 0.1875),
    (52, 5.25, 0.1875),
    (50, 5.625, 0.1875), # comp on 4
    (57, 5.625, 0.1875),
    (52, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone - Dante: Short motif, sing it, leave it hanging, come back and finish
# Motif: F - Gb - Bb - F (start at 1.5s) -> rest on 4th beat
sax_notes = [
    (84, 1.5, 0.375), # F
    (86, 1.875, 0.375), # Gb
    (81, 2.25, 0.375), # Bb
    (84, 2.625, 0.375), # F
    (84, 3.0, 0.375), # F (rest on 4th beat, start repeat)
    (86, 3.375, 0.375), # Gb
    (81, 3.75, 0.375), # Bb
    (84, 4.125, 0.375), # F
    (84, 4.5, 0.375), # F (rest on 4th beat, start repeat)
    (86, 4.875, 0.375), # Gb
    (81, 5.25, 0.375), # Bb
    (84, 5.625, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1& 
    (42, 1.6875, 0.1875),# Hihat on 2
    (38, 1.875, 0.375),  # Snare on 3
    (42, 1.875, 0.1875), # Hihat on 3&
    (42, 2.0625, 0.1875),# Hihat on 4
    (36, 2.25, 0.375),   # Kick on 2
    (42, 2.25, 0.1875),  # Hihat on 2&
    (42, 2.4375, 0.1875),# Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4&
    (42, 2.8125, 0.1875),# Hihat on 1
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1& 
    (42, 3.1875, 0.1875),# Hihat on 2
    (38, 3.375, 0.375),  # Snare on 3
    (42, 3.375, 0.1875), # Hihat on 3&
    (42, 3.5625, 0.1875),# Hihat on 4
    (36, 3.75, 0.375),   # Kick on 2
    (42, 3.75, 0.1875),  # Hihat on 2&
    (42, 3.9375, 0.1875),# Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4&
    (42, 4.3125, 0.1875),# Hihat on 1
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1& 
    (42, 4.6875, 0.1875),# Hihat on 2
    (38, 4.875, 0.375),  # Snare on 3
    (42, 4.875, 0.1875), # Hihat on 3&
    (42, 5.0625, 0.1875),# Hihat on 4
    (36, 5.25, 0.375),   # Kick on 2
    (42, 5.25, 0.1875),  # Hihat on 2&
    (42, 5.4375, 0.1875),# Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4&
    (42, 5.8125, 0.1875) # Hihat on 1
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
