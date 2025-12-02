
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Dm7 = D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),   # A
    pretty_midi.Note(velocity=80, pitch=68, start=2.75, end=3.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),   # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.0),   # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),   # G
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=80, pitch=68, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),   # B
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),   # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),   # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.75, end=6.0),   # Eb
]

# Diane: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Dm7 = D F A C
# comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),

    # Bar 3: Dm7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),

    # Bar 4: Dm7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),
]

# You: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D F A C
# Motif: D -> F -> A -> rest
# Then repeat with some rhythmic variation
sax_notes = [
    # First phrase: D -> F -> A -> rest
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D on beat 1
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75), # F on 2
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875), # A on 3
    # Leave it hanging
    # Second phrase: D -> A -> rest -> F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D on beat 3
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75), # A on 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375), # D on beat 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.625, end=3.75), # F on 4
]

# Add drum notes to drum instrument
for note in drum_notes:
    drums.notes.append(note)

# Add bass notes to bass instrument
for note in bass_notes:
    bass.notes.append(note)

# Add piano notes to piano instrument
for note in piano_notes:
    piano.notes.append(note)

# Add sax notes to sax instrument
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
