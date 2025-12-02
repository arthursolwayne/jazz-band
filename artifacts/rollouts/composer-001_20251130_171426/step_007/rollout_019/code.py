
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
bar1_start = 0.0
bar1_end = 1.5
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.0, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.5, end=bar1_start + 1.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.0, end=bar1_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.75, end=bar1_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, chromatic approaches
bass_notes = []
bar_start = 1.5
bar_duration = 1.5
time = bar_start

for bar in range(3):
    # Fm: F, Ab, Bb, D, Eb, G, A
    # Walking bass line in Fm (F7)
    # Chromatic approaches to F, Ab, Bb, D
    # Bar 2: F -> Eb -> D -> F
    # Bar 3: Ab -> G -> F -> Ab
    # Bar 4: Bb -> A -> G -> Bb
    if bar == 0:
        notes = [76, 71, 69, 76]
    elif bar == 1:
        notes = [77, 76, 76, 77]
    elif bar == 2:
        notes = [68, 68, 71, 68]
    for i, note in enumerate(notes):
        start = time + i * 0.375
        end = start + 0.375
        bass_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))
    time += bar_duration

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = []
time = bar_start
for bar in range(3):
    # F7 = F, A, C, Eb
    # Bb7 = Bb, D, F, Ab
    # Ab7 = Ab, C, Eb, G
    if bar == 0:
        # F7 on 1 and 3
        notes = [76, 79, 72, 71]
    elif bar == 1:
        # Bb7 on 1 and 3
        notes = [71, 74, 76, 77]
    elif bar == 2:
        # Ab7 on 1 and 3
        notes = [77, 80, 71, 74]
    for i, note in enumerate(notes):
        start = time + i * 0.375
        end = start + 0.375
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))
    time += bar_duration

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
time = bar_start
# First bar: F Ab Bb (Fm triad)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + 0.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=77, start=time + 0.375, end=time + 0.75))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 0.75, end=time + 1.125))
# Leave it hanging on the last note of the bar
# Second bar: D Ab (chromatic approach to F)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time + 1.5, end=time + 1.875))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=77, start=time + 1.875, end=time + 2.25))
# Third bar: F Eb (chromatic approach to D)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time + 3.0, end=time + 3.375))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 3.375, end=time + 3.75))
# Final bar: Bb F (resolution)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 4.5, end=time + 4.875))
sax_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time + 4.875, end=time + 5.25))

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
