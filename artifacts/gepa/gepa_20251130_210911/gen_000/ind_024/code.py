
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Sax, Bass, Piano, Drums
# Bar 2 (1.5 - 3.0s)
# Marcus (bass): Walking line with chromatic approaches
bass_notes = [
    (36, 1.5), (37, 1.75), (35, 2.0), (36, 2.25),
    (38, 2.5), (37, 2.75), (36, 3.0)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane (piano): 7th chords on 2 and 4
piano_notes = [
    (59, 2.0), (64, 2.0), (61, 2.0), (62, 2.0),  # F7
    (57, 3.0), (62, 3.0), (59, 3.0), (60, 3.0)   # C7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante (sax): Motif in F
sax_notes = [
    (62, 1.5), (65, 1.75), (62, 2.0),
    (60, 2.5), (62, 2.75), (65, 3.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 3 (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    (38, 3.0), (37, 3.25), (36, 3.5), (37, 3.75),
    (35, 4.0), (36, 4.25), (38, 4.5)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords
piano_notes = [
    (59, 3.5), (64, 3.5), (61, 3.5), (62, 3.5),  # F7
    (57, 4.5), (62, 4.5), (59, 4.5), (60, 4.5)   # C7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Motif variation
sax_notes = [
    (60, 3.0), (62, 3.25), (65, 3.5),
    (62, 4.0), (60, 4.25), (62, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 4 (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    (37, 4.5), (38, 4.75), (36, 5.0), (37, 5.25),
    (35, 5.5), (36, 5.75), (37, 6.0)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords
piano_notes = [
    (59, 5.0), (64, 5.0), (61, 5.0), (62, 5.0),  # F7
    (57, 6.0), (62, 6.0), (59, 6.0), (60, 6.0)   # C7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Motif resolution
sax_notes = [
    (62, 4.5), (65, 4.75), (62, 5.0),
    (62, 5.5), (65, 5.75), (62, 6.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums continue
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
