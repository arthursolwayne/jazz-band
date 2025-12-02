
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice.

# Dm7 chord: D F A C
# Bass line in D minor: D -> C -> Bb -> B -> A -> G -> F -> E -> D -> C -> Bb -> B -> A -> G -> F -> E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.5),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4.
# Dm7 = D F A C
# Comping pattern: play Dm7 on beat 2 and 4 of each bar
piano_notes = [
    # Bar 2, beat 2 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # C
    # Bar 2, beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # C
    # Bar 3, beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # C
    # Bar 3, beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),  # C
    # Bar 4, beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # C
    # Bar 4, beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D - F - A (quarter notes), then hold A for a beat, then resolve to C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.75),  # A (hold)
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=6.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
