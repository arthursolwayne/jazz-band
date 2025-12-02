
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
# Bass: Walking line, chromatic approaches
bass_notes = [
    (60, 1.5), (61, 1.75), (62, 2.0), (63, 2.25),
    (64, 2.5), (65, 2.75), (66, 3.0), (67, 3.25),
    (68, 3.5), (69, 3.75), (70, 4.0), (71, 4.25),
    (72, 4.5), (73, 4.75), (74, 5.0), (75, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.75), (64, 1.75), (67, 1.75), (71, 1.75),
    # Bar 3
    (62, 3.25), (66, 3.25), (69, 3.25), (73, 3.25),
    # Bar 4
    (64, 4.75), (68, 4.75), (71, 4.75), (75, 4.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Melody - short motif, make it sing
sax_notes = [
    (62, 1.5), (64, 1.75), (65, 2.0), (64, 2.25),
    (62, 2.5), (64, 2.75), (65, 3.0), (67, 3.25),
    (65, 3.5), (64, 3.75), (62, 4.0), (64, 4.25),
    (65, 4.5), (67, 4.75), (65, 5.0), (64, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums continue for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Set tempo to 120 BPM
midi.tempo = 120 * pretty_midi.MIDI_TEMPO_RESOLUTION / 60

# Save the MIDI file
midi.write("dante_intro.mid")
