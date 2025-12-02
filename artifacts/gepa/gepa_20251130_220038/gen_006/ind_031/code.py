
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

# Bass line: walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5), (63, 1.875), (60, 2.25), (61, 2.625),
    # Bar 3
    (62, 3.0), (64, 3.375), (62, 3.75), (60, 4.125),
    # Bar 4
    (62, 4.5), (63, 4.875), (60, 5.25), (61, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875), (64, 1.875), (67, 1.875), (70, 1.875),
    # Bar 3
    (62, 3.375), (64, 3.375), (67, 3.375), (70, 3.375),
    # Bar 4
    (62, 4.875), (64, 4.875), (67, 4.875), (70, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D F A C
sax_notes = [
    (62, 1.5), (64, 1.625), (67, 1.75), (70, 1.875),  # Start the motif
    (62, 2.625), (64, 2.75), (67, 2.875), (70, 3.0),   # Re-enter and finish it
    (62, 3.75), (64, 3.875), (67, 4.0), (70, 4.125)    # Echo it one last time
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
