
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in
# Bass - Marcus: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=70, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=70, pitch=39, start=2.25, end=2.625), # Eb2 (chromatic)
    pretty_midi.Note(velocity=70, pitch=43, start=2.625, end=3.0),  # A2
]

# Piano - Diane: open voicings, different chord each bar, resolve on the last
# Bar 2: D7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F#4
]

# Sax - Dante: short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G4
]

# Bar 3: Everyone in
# Bass - Marcus: walking line
bass_notes.extend([
    pretty_midi.Note(velocity=70, pitch=45, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=70, pitch=43, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=70, pitch=44, start=3.75, end=4.125),  # Bb2
    pretty_midi.Note(velocity=70, pitch=48, start=4.125, end=4.5),   # D3
])

# Piano - Diane: G7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # B4
])

# Sax - Dante: continuation of motif, build and release
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A4
])

# Bar 4: Everyone in
# Bass - Marcus: walking line
bass_notes.extend([
    pretty_midi.Note(velocity=70, pitch=50, start=4.5, end=4.875),  # F3
    pretty_midi.Note(velocity=70, pitch=48, start=4.875, end=5.25),  # D3
    pretty_midi.Note(velocity=70, pitch=49, start=5.25, end=5.625),  # Eb3
    pretty_midi.Note(velocity=70, pitch=53, start=5.625, end=6.0),   # G3
])

# Piano - Diane: resolve to Dmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B4
])

# Sax - Dante: finish the motif, release
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
])

# Drums - Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=95, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),   # Hihat on 4
])

# Assign notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
