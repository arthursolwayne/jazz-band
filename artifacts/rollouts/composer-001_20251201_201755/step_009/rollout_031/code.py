
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
# Bar 2: F, C, B, C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=77, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=3.0),  # C
    # Bar 3: G, D, C#, D
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=4.125), # C#
    pretty_midi.Note(velocity=80, pitch=79, start=4.125, end=4.5),  # D
    # Bar 4: A, E, D#, E
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=80, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last chord of each bar
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875), # E
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375), # F
])
# Bar 4: Amaj7 (A C E G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875), # G
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Bb - C (F G Bb C), played over 3 bars
# Bar 2: F, G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25), # G
]
# Bar 3: Bb, rest
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375), # Bb
])
# Bar 4: C, finish the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.875), # C
])
sax.notes.extend(sax_notes)

# Drums: Bars 2-4, same pattern as Bar 1
for i in range(2):
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0, note.end + 3.0)
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
