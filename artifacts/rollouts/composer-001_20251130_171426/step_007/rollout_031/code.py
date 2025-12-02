
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in F, chromatic approaches, no repeating notes
bass_notes = [
    (45, 1.5), (47, 1.875), (46, 2.25), (44, 2.625),
    (45, 3.0), (47, 3.375), (46, 3.75), (44, 4.125),
    (45, 4.5), (47, 4.875), (46, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    (62, 2.0), (66, 2.0), (67, 2.0), (69, 2.0),  # F7
    (62, 3.0), (66, 3.0), (67, 3.0), (69, 3.0),  # F7
    (62, 4.0), (66, 4.0), (67, 4.0), (69, 4.0)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax - short motif, starts on 1.5s, ends on 2.25s, leaves it hanging
sax_notes = [
    (66, 1.5), (69, 1.75), (67, 2.0), (66, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Re-enter sax on bar 3 to complete the phrase
sax_notes = [
    (66, 3.5), (69, 3.75), (67, 4.0), (66, 4.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Re-enter sax again on bar 4 to give it closure
sax_notes = [
    (66, 4.5), (69, 4.75), (67, 5.0), (66, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
