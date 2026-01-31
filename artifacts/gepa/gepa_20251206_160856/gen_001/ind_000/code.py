
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2 (MIDI 38) to G2 (MIDI 43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.125),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),   # G2
    pretty_midi.Note(velocity=80, pitch=41, start=2.5, end=2.875),   # F2 (chromatic approach)
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=2.875, end=3.25),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.25, end=3.5),    # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=3.5, end=3.875),   # G2
    pretty_midi.Note(velocity=80, pitch=41, start=3.875, end=4.25),  # F2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.25, end=4.625),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.625, end=4.875),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),   # G2
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.0),  # C5
    # Bar 3: Gm7 (G-Bb-D-F)
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=80, pitch=73, start=2.5, end=3.0),  # Bb4
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=3.0),  # F4
    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=4.0),  # C4
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=4.0),  # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=4.0),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=4.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C, D
sax_notes = [
    # Bar 2: Start with a short motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # F4
    # Leave it hanging
    # Bar 3: Return and finish the motif
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # C5
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # D4
    # Bar 4: End with a question
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.125), # A4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    kick3_start = start + 1.125
    kick3_end = kick3_start + 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick3_start, end=kick3_end))
    # Snare on 2 and 4
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare4_start = start + 1.875
    snare4_end = snare4_start + 0.125
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare4_start, end=snare4_end))
    # Hihat on every eighth
    for i in range(0, 8):
        hihat_start = start + (i * 0.375)
        hihat_end = hihat_start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
