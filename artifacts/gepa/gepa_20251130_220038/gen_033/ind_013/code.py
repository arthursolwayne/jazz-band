
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0), # F

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5), # Bb

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=90, pitch=75, start=5.625, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.625), # C#

    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375), # F#
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375), # C#

    # Bar 3: G7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=81, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=84, start=3.75, end=4.125), # F#

    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875), # F#

    # Bar 4: D7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=72, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.625), # C#

    pretty_midi.Note(velocity=95, pitch=72, start=6.0, end=6.375), # D
    pretty_midi.Note(velocity=90, pitch=74, start=6.0, end=6.375), # F#
    pretty_midi.Note(velocity=90, pitch=77, start=6.0, end=6.375), # A
    pretty_midi.Note(velocity=90, pitch=81, start=6.0, end=6.375), # C#
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.875), # F#
    pretty_midi.Note(velocity=105, pitch=77, start=1.875, end=2.25), # A

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=105, pitch=77, start=3.0, end=3.375), # A

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=105, pitch=77, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # D
]
sax.notes.extend(sax_notes)

# Fill the bar with hihat
for bar in range(3):
    start = 1.5 + bar * 1.5
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)

# Add the rest of the hihat
for bar in range(3):
    start = 1.5 + bar * 1.5
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)

# Add the kick and snare in the full bars
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
