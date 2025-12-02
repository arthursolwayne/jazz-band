
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

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (65, 2.625),
    (67, 3.0), (69, 3.375), (68, 3.75), (70, 4.125),
    (72, 4.5), (74, 4.875), (73, 5.25), (75, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5), (67, 1.5), (71, 1.5),  # D7
    (67, 1.875), (70, 1.875), (74, 1.875),  # F#7
    # Bar 3
    (64, 3.0), (67, 3.0), (71, 3.0),  # D7
    (67, 3.375), (70, 3.375), (74, 3.375),  # F#7
    # Bar 4
    (64, 4.5), (67, 4.5), (71, 4.5),  # D7
    (67, 4.875), (70, 4.875), (74, 4.875)   # F#7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Sax: Dante, motif - start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5), (64, 1.625), (66, 1.75), (64, 2.0),  # first phrase
    (62, 2.25), (64, 2.375), (66, 2.5), (64, 2.75),  # second phrase
    (62, 3.0), (64, 3.125), (65, 3.25), (64, 3.5),  # third phrase
    (62, 3.75), (64, 3.875), (65, 4.0), (64, 4.25),  # fourth phrase
    (62, 4.5), (64, 4.625), (66, 4.75), (64, 5.0)   # fifth phrase
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
