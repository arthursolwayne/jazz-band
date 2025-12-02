
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

# Bass line (Marcus): Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (42, 2.25),
    (45, 2.5), (46, 2.75), (44, 3.0), (42, 3.25),
    (45, 3.5), (46, 3.75), (44, 4.0), (42, 4.25),
    (45, 4.5), (46, 4.75), (44, 5.0), (42, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (59, 1.75), (62, 1.75), (64, 1.75), (66, 1.75),  # F7
    (59, 2.25), (62, 2.25), (64, 2.25), (66, 2.25),  # F7
    # Bar 3
    (59, 3.25), (62, 3.25), (64, 3.25), (66, 3.25),  # F7
    (59, 3.75), (62, 3.75), (64, 3.75), (66, 3.75),  # F7
    # Bar 4
    (59, 4.75), (62, 4.75), (64, 4.75), (66, 4.75),  # F7
    (59, 5.25), (62, 5.25), (64, 5.25), (66, 5.25)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.625), (62, 1.75), (60, 1.875),
    (62, 3.0), (64, 3.125), (62, 3.25), (60, 3.375),
    (62, 4.5), (64, 4.625), (62, 4.75), (60, 4.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
