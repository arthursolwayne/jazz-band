
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Double Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 to 1.5s (4 beats)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth note (0.0, 0.375, 0.75, 1.125, 1.5, ...)
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line in Dm, chromatic approaches, no repeated notes
# Dm: D F A C (scale: D Eb F G A Bb B C)
# Walking bass: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D...
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Chords on 2 and 4: bar 2 on beat 2, bar 3 on beat 2, bar 4 on beat 2
piano_notes = [
    # Bar 2: Dm7 on beat 2 (start=2.25)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # C
    # Bar 3: Dm7 on beat 2 (start=3.75)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C
    # Bar 4: Dm7 on beat 2 (start=5.25)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante: One short motif, make it sing
# Dm scale: D Eb F G A Bb B C
# Motif: D, F, G, A -> D, F, G, A -> D, F, G, A (but not a scale run)
# So we'll ascend but cut the last note, leave it hanging

sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save("dante_russo_intro.mid")
