
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
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (43)
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.0),
    # G2 (43)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to A2 (45)
    pretty_midi.Note(velocity=70, pitch=44, start=2.375, end=2.5625),
    # Bar 3: A2 (45)
    pretty_midi.Note(velocity=90, pitch=45, start=2.5625, end=2.9375),
    # Chromatic approach to D3 (50)
    pretty_midi.Note(velocity=70, pitch=49, start=2.9375, end=3.125),
    # D3 (50)
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.5),
    # Chromatic approach to E3 (52)
    pretty_midi.Note(velocity=70, pitch=51, start=3.5, end=3.6875),
    # Bar 4: E3 (52)
    pretty_midi.Note(velocity=90, pitch=52, start=3.6875, end=4.0625),
    # Chromatic approach to A3 (57)
    pretty_midi.Note(velocity=70, pitch=56, start=4.0625, end=4.25),
    # A3 (57)
    pretty_midi.Note(velocity=90, pitch=57, start=4.25, end=4.625),
    # Chromatic approach to D4 (62)
    pretty_midi.Note(velocity=70, pitch=61, start=4.625, end=4.8125),
    # D4 (62)
    pretty_midi.Note(velocity=90, pitch=62, start=4.8125, end=5.1875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.0),  # C#4
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.5625, end=3.0),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=2.5625, end=3.0),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.5625, end=3.0),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=2.5625, end=3.0),  # F4
])
# Bar 4: A7 (A-C#-E-G)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=69, start=3.6875, end=4.1875),  # A4
    pretty_midi.Note(velocity=80, pitch=74, start=3.6875, end=4.1875),  # C#5
    pretty_midi.Note(velocity=90, pitch=72, start=3.6875, end=4.1875),  # E5
    pretty_midi.Note(velocity=80, pitch=69, start=3.6875, end=4.1875),  # G4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F#4 (67), A4 (71), B4 (73)
# Start at 1.5s, end at 2.0s (first two notes), then leave it hanging until 3.0s, then finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=100, pitch=73, start=3.25, end=3.5),  # B4
]
sax.notes.extend(sax_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
for i in range(2):
    drum_start = 1.5 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start, end=drum_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start + 1.125, end=drum_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=drum_start + 0.75, end=drum_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=drum_start + 1.875, end=drum_start + 2.0)
    # Hi-hat on every eighth
    for j in range(8):
        start = drum_start + j * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

# Bar 3: 3.0 - 4.5s
for i in range(2):
    drum_start = 3.0 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start, end=drum_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start + 1.125, end=drum_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=drum_start + 0.75, end=drum_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=drum_start + 1.875, end=drum_start + 2.0)
    # Hi-hat on every eighth
    for j in range(8):
        start = drum_start + j * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

# Bar 4: 4.5 - 6.0s
for i in range(2):
    drum_start = 4.5 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start, end=drum_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=drum_start + 1.125, end=drum_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=drum_start + 0.75, end=drum_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=drum_start + 1.875, end=drum_start + 2.0)
    # Hi-hat on every eighth
    for j in range(8):
        start = drum_start + j * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
