
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # F2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (Dmaj7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # D5
    # Bar 3 (Em7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # D5
    # Bar 4 (G7)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # F5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),  # B4
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # A4
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),  # B4
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),  # A4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    kick_start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 0.75, end=kick_start + 1.125)
# Snare on 2 and 4
for bar in [2, 3, 4]:
    snare_start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 0.75, end=snare_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 1.875, end=snare_start + 2.0)
# Hihat on every eighth
for bar in [2, 3, 4]:
    snare_start = (bar - 1) * 1.5
    for i in range(8):
        start = snare_start + (i * 0.1875)
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
