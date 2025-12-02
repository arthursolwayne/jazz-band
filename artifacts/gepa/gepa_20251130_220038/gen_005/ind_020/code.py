
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
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375), (42, 1.5)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (37, 1.5), (38, 1.75), (36, 2.0), (37, 2.25),
    (39, 2.5), (40, 2.75), (38, 3.0), (37, 3.25),
    (35, 3.5), (36, 3.75), (38, 4.0), (39, 4.25),
    (41, 4.5), (42, 4.75), (40, 5.0), (39, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.75), (67, 1.75), (64, 1.75), (69, 1.75),
    # Bar 3
    (60, 3.25), (65, 3.25), (62, 3.25), (67, 3.25),
    # Bar 4
    (62, 4.75), (67, 4.75), (64, 4.75), (69, 4.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (66, 1.75), (67, 2.0), (64, 2.25),
    (62, 2.5), (66, 2.75), (67, 3.0), (64, 3.25),
    (62, 3.5), (66, 3.75), (67, 4.0), (64, 4.25),
    (62, 4.5), (66, 4.75), (67, 5.0), (64, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.875))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.25))
    # Hihat every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.125, end=start + i * 0.125 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")
