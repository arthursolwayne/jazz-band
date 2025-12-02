
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.75),
    (36, 1.125), (38, 1.5), (42, 1.875),
    (42, 2.25), (42, 2.625), (42, 3.0)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (65, 1.5), (67, 1.875), (64, 2.25), (62, 2.625),
    (65, 3.0), (67, 3.375), (64, 3.75), (62, 4.125),
    (65, 4.5), (67, 4.875), (64, 5.25), (62, 5.625)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp with space
piano_notes = [
    # Bar 2
    (72, 1.875), (74, 1.875), (76, 1.875), (79, 1.875),
    # Bar 3
    (72, 3.375), (74, 3.375), (76, 3.375), (79, 3.375),
    # Bar 4
    (72, 4.875), (74, 4.875), (76, 4.875), (79, 4.875)
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax melody: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (64), A (65), B (66), D (62), C# (63), B (66), A (65)
sax_notes = [
    (62, 1.5), (64, 1.875), (65, 2.25), (66, 2.625),
    (62, 3.0), (63, 3.375), (66, 3.75), (65, 4.125),
    (62, 4.5), (64, 4.875), (65, 5.25), (66, 5.625)
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.125))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.45))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 0.875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.2))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.075))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
