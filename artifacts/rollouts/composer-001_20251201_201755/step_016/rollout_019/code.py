
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

# Bass: Marcus - walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 - root
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # G2 - fifth
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # F#2 - chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2 - root
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # E5
]
# Bar 3: Bmin7 (B D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # F5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # A5
])
# Bar 4: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # F5
])
piano.notes.extend(piano_notes)

# Sax: Dante - motif in F
# Motif: F (65) - E (64) - D (62) - F (65)
# Start at 1.5s, then leave it hanging until 3.0s, then return at 4.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # F4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: continue in bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    drum_start = 1.5 + i * 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start, end=drum_start + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=drum_start, end=drum_start + 0.1875)

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    drum_start = 3.0 + i * 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start, end=drum_start + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=drum_start, end=drum_start + 0.1875)

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    drum_start = 4.5 + i * 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start, end=drum_start + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=drum_start, end=drum_start + 0.1875)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
