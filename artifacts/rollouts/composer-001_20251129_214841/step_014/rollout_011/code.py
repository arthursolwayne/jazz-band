
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # C#4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # E4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),  # G#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # A4
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),   # A#4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # B4
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # C5
    pretty_midi.Note(velocity=90, pitch=73, start=5.625, end=6.0),   # C#5
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # B4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),   # C5
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # B4
]
piano.notes.extend(piano_notes)

# Drums in bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Saxophone (Dante) - motif starts at bar 2
# Melody: C - E - B - C (play on beat 1, 2, 3, 4 of bar 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),   # C4
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
