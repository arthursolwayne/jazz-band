
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # D
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=2.25),  # F7 - F
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=2.25),  # F7 - Bb
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=2.25),  # F7 - E
    pretty_midi.Note(velocity=95, pitch=79, start=1.5, end=2.25),  # F7 - Ab
    pretty_midi.Note(velocity=95, pitch=65, start=2.625, end=3.0), # F7 - F
    pretty_midi.Note(velocity=95, pitch=72, start=2.625, end=3.0), # F7 - Bb
    pretty_midi.Note(velocity=95, pitch=76, start=2.625, end=3.0), # F7 - E
    pretty_midi.Note(velocity=95, pitch=79, start=2.625, end=3.0), # F7 - Ab
]

# Sax: Motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G#
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),  # G
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.125),  # C#
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),   # C
])

# Piano: 7th chords on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.75),  # F7 - F
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.75),  # F7 - Bb
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.75),  # F7 - E
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.75),  # F7 - Ab
    pretty_midi.Note(velocity=95, pitch=65, start=4.125, end=4.5), # F7 - F
    pretty_midi.Note(velocity=95, pitch=72, start=4.125, end=4.5), # F7 - Bb
    pretty_midi.Note(velocity=95, pitch=76, start=4.125, end=4.5), # F7 - E
    pretty_midi.Note(velocity=95, pitch=79, start=4.125, end=4.5), # F7 - Ab
])

# Sax: Continue motif with variation
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),   # G
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),   # C
])

# Piano: 7th chords on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=5.25),  # F7 - F
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=5.25),  # F7 - Bb
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=5.25),  # F7 - E
    pretty_midi.Note(velocity=95, pitch=79, start=4.5, end=5.25),  # F7 - Ab
    pretty_midi.Note(velocity=95, pitch=65, start=5.625, end=6.0), # F7 - F
    pretty_midi.Note(velocity=95, pitch=72, start=5.625, end=6.0), # F7 - Bb
    pretty_midi.Note(velocity=95, pitch=76, start=5.625, end=6.0), # F7 - E
    pretty_midi.Note(velocity=95, pitch=79, start=5.625, end=6.0), # F7 - Ab
])

# Sax: End with a question — leave it hanging
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # G#
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),   # G
])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
])

# Add the notes to their respective instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_in_f.mid")
