
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

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),
    (62, 3.0), (64, 3.375), (63, 3.75), (60, 4.125),
    (62, 4.5), (64, 4.875), (63, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 2.25), (67, 2.25), (69, 2.25), (71, 2.25),
    (62, 3.0), (65, 3.0), (67, 3.0), (69, 3.0),
    # Bar 3
    (62, 3.75), (67, 3.75), (69, 3.75), (71, 3.75),
    (62, 4.5), (65, 4.5), (67, 4.5), (69, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): One short motif, make it sing, leave it hanging, return to finish
sax_notes = [
    # Bar 2
    (62, 1.5), (64, 1.875), (65, 2.25),
    # Bar 3
    (64, 3.0), (62, 3.375), (60, 3.75),
    # Bar 4
    (62, 4.125), (64, 4.5), (65, 4.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
