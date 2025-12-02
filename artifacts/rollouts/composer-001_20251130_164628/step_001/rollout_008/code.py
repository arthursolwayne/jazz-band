
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (45, 1.5), (46, 1.875), (44, 2.25), (45, 2.625),
    # Bar 3
    (47, 3.0), (48, 3.375), (46, 3.75), (47, 4.125),
    # Bar 4
    (49, 4.5), (50, 4.875), (48, 5.25), (49, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875), (65, 1.875), (67, 1.875), (70, 1.875),
    # Bar 3
    (62, 3.375), (65, 3.375), (67, 3.375), (70, 3.375),
    # Bar 4
    (62, 4.875), (65, 4.875), (67, 4.875), (70, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Sax: short motif, starts on beat 1 of bar 2, leaves it hanging
sax_notes = [
    (62, 1.5), (65, 1.875), (67, 2.25), (65, 2.625),
    (62, 3.0), (65, 3.375), (69, 3.75), (67, 4.125),
    (62, 4.5), (65, 4.875), (67, 5.25), (65, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
