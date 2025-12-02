
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: F, Bb, Ab, G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),     # Bb
    pretty_midi.Note(velocity=95, pitch=68, start=2.0, end=2.25),     # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),    # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),    # G (reprise)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),     # Bb (reprise)
]
sax.notes.extend(sax_notes)

# Bass line: walking with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=75, pitch=48, start=1.75, end=2.0),    # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25),    # G
    pretty_midi.Note(velocity=75, pitch=46, start=2.25, end=2.5),    # E
    pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.75),    # F
    pretty_midi.Note(velocity=75, pitch=48, start=2.75, end=3.0),    # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),    # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=75, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=85, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),
    pretty_midi.Note(velocity=75, pitch=62, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif variation: F, C, Eb, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),    # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),     # C
    pretty_midi.Note(velocity=95, pitch=65, start=3.5, end=3.75),     # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),    # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),    # D (reprise)
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),     # C (reprise)
]
sax.notes.extend(sax_notes)

# Bass line: walking with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.25),    # F
    pretty_midi.Note(velocity=75, pitch=48, start=3.25, end=3.5),    # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),    # G
    pretty_midi.Note(velocity=75, pitch=46, start=3.75, end=4.0),    # E
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),    # F
    pretty_midi.Note(velocity=75, pitch=48, start=4.25, end=4.5),    # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),    # F7
    pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=75, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=85, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),
    pretty_midi.Note(velocity=75, pitch=62, start=4.25, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif variation: F, G, Ab, G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75),    # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),     # G
    pretty_midi.Note(velocity=95, pitch=68, start=5.0, end=5.25),     # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),    # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75),    # F (reprise)
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),     # G (reprise)
]
sax.notes.extend(sax_notes)

# Bass line: walking with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.75),    # F
    pretty_midi.Note(velocity=75, pitch=48, start=4.75, end=5.0),    # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),    # G
    pretty_midi.Note(velocity=75, pitch=46, start=5.25, end=5.5),    # E
    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.75),    # F
    pretty_midi.Note(velocity=75, pitch=48, start=5.75, end=6.0),    # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),    # F7
    pretty_midi.Note(velocity=85, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=75, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),
    pretty_midi.Note(velocity=85, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),
    pretty_midi.Note(velocity=75, pitch=62, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Add drum fills in bar 2 and 3
# Bar 2: Fill on beat 3 with a closed hihat
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # Hihat on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Fill on beat 3 with a snare and open hihat
drum_notes = [
    pretty_midi.Note(velocity=95, pitch=38, start=3.75, end=4.0),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.0), # Open hihat on 3
]
drums.notes.extend(drum_notes)

# Add final drum hit on beat 4 of bar 4
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=5.75, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
