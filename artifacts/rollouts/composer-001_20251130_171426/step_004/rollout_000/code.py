
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.125), (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4 (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5), (64, 1.875), (62, 2.25), (60, 2.625),
    # Bar 3
    (62, 3.0), (64, 3.375), (62, 3.75), (60, 4.125),
    # Bar 4
    (62, 4.5), (64, 4.875), (62, 5.25), (60, 5.625)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.875), (71, 1.875), (69, 1.875), (73, 1.875),  # D7
    (69, 2.25), (73, 2.25), (71, 2.25), (75, 2.25),  # F#7
    # Bar 3
    (67, 3.375), (71, 3.375), (69, 3.375), (73, 3.375),  # D7
    (69, 3.75), (73, 3.75), (71, 3.75), (75, 3.75),  # F#7
    # Bar 4
    (67, 4.875), (71, 4.875), (69, 4.875), (73, 4.875),  # D7
    (69, 5.25), (73, 5.25), (71, 5.25), (75, 5.25)   # F#7
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: D - F# - B - D
# Bar 2: Start motif
sax_notes = [
    (62, 1.5), (67, 1.875), (69, 2.25), (62, 2.625),  # D - F# - B - D
    # Bar 3: Leave it hanging, no sax
    # Bar 4: Come back and finish the motif
    (62, 4.5), (67, 4.875), (69, 5.25), (62, 5.625)
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875),
    (42, 2.0), (42, 2.125), (42, 2.25), (42, 2.375), (36, 2.625), (38, 3.0),
    (42, 2.625), (42, 2.75), (42, 2.875), (42, 3.0),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.0), (42, 3.125), (42, 3.25), (42, 3.375),
    (42, 3.5), (42, 3.625), (42, 3.75), (42, 3.875), (36, 4.125), (38, 4.5),
    (42, 4.125), (42, 4.25), (42, 4.375), (42, 4.5),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.5), (42, 4.625), (42, 4.75), (42, 4.875),
    (42, 5.0), (42, 5.125), (42, 5.25), (42, 5.375), (36, 5.625), (38, 6.0),
    (42, 5.625), (42, 5.75), (42, 5.875), (42, 6.0)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
