
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

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (55, 1.5), (57, 1.875), (53, 2.25), (50, 2.625),
    (55, 3.0), (57, 3.375), (53, 3.75), (50, 4.125),
    (55, 4.5), (57, 4.875), (53, 5.25), (50, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (57, 3.0), (60, 3.0), (62, 3.0), (64, 3.0), (67, 3.0),  # Fm7 at bar 2
    (57, 4.5), (60, 4.5), (62, 4.5), (64, 4.5), (67, 4.5),  # Fm7 at bar 3
    (57, 6.0), (60, 6.0), (62, 6.0), (64, 6.0), (67, 6.0)   # Fm7 at bar 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Short motif, starts on beat 1 of bar 2, ends on beat 3 of bar 4
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (60, 2.25),
    (62, 2.5), (64, 2.75), (62, 3.0), (60, 3.25),
    (62, 3.5), (64, 3.75), (62, 4.0), (60, 4.25),
    (62, 4.5), (64, 4.75), (62, 5.0), (60, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
