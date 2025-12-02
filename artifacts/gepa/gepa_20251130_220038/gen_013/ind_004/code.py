
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start on D (62), then Bb (60), then F (53), leave it hanging
sax_notes = [
    (62, 1.5), (60, 1.875), (53, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (61, 1.75), (60, 2.0), (59, 2.25),
    (62, 2.5), (61, 2.75), (60, 3.0), (59, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (62, 1.875), (67, 1.875), (64, 1.875), (60, 1.875),
    (62, 2.625), (67, 2.625), (64, 2.625), (60, 2.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: return to motif, finish it on D
sax_notes = [
    (62, 3.0), (60, 3.375), (53, 3.75), (62, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 3.0), (61, 3.25), (60, 3.5), (59, 3.75),
    (62, 4.0), (61, 4.25), (60, 4.5), (59, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Dm7 on 2 and 4
    (62, 3.375), (67, 3.375), (64, 3.375), (60, 3.375),
    (62, 4.125), (67, 4.125), (64, 4.125), (60, 4.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: variation of motif, end on Bb
sax_notes = [
    (62, 4.5), (60, 4.875), (53, 5.25), (60, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 4.5), (61, 4.75), (60, 5.0), (59, 5.25),
    (62, 5.5), (61, 5.75), (60, 6.0), (59, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Dm7 on 2 and 4
    (62, 4.875), (67, 4.875), (64, 4.875), (60, 4.875),
    (62, 5.625), (67, 5.625), (64, 5.625), (60, 5.625)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
