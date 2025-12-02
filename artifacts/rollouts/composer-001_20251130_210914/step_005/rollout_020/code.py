
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),  # 1
    (36, 0.75), (38, 1.125), (42, 1.125), # 2
    (36, 1.5), (38, 1.875), (42, 1.875),  # 3
    (36, 2.25), (38, 2.625), (42, 2.625)  # 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, time, time + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    (64, 1.5), (65, 1.75), (63, 2.0), (62, 2.25),  # Fm walking line
    (64, 2.5), (65, 2.75), (63, 3.0), (62, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.75), (67, 1.75), (69, 1.75), (71, 1.75),  # F7 on 2
    (65, 2.25), (68, 2.25), (70, 2.25), (72, 2.25)   # Ab7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Dante: Motif starts here, one short phrase
sax_notes = [
    (64, 1.5), (66, 1.75), (67, 2.0), (66, 2.25),  # F - G - G# - G
    (64, 2.5), (66, 2.75), (67, 3.0), (66, 3.25)   # F - G - G# - G
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(110, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    (64, 3.0), (65, 3.25), (63, 3.5), (62, 3.75),  # Fm walking line
    (64, 4.0), (65, 4.25), (63, 4.5), (62, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.25), (67, 3.25), (69, 3.25), (71, 3.25),  # F7 on 2
    (65, 3.75), (68, 3.75), (70, 3.75), (72, 3.75)   # Ab7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Dante: Motif continues, leave it hanging
sax_notes = [
    (64, 3.0), (66, 3.25), (67, 3.5), (66, 3.75),  # F - G - G# - G
    (64, 4.0), (66, 4.25), (67, 4.5), (66, 4.75)   # F - G - G# - G
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(110, note, time, time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    (64, 4.5), (65, 4.75), (63, 5.0), (62, 5.25),  # Fm walking line
    (64, 5.5), (65, 5.75), (63, 6.0), (62, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 4.75), (67, 4.75), (69, 4.75), (71, 4.75),  # F7 on 2
    (65, 5.25), (68, 5.25), (70, 5.25), (72, 5.25)   # Ab7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Dante: Motif ends here, finish it
sax_notes = [
    (64, 4.5), (66, 4.75), (67, 5.0), (66, 5.25),  # F - G - G# - G
    (64, 5.5), (66, 5.75), (67, 6.0), (66, 6.25)   # F - G - G# - G
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(110, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),  # 1
    (36, 5.25), (38, 5.625), (42, 5.625), # 2
    (36, 5.75), (38, 6.125), (42, 6.125),  # 3
    (36, 6.5), (38, 6.875), (42, 6.875)    # 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(100, note, time, time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
