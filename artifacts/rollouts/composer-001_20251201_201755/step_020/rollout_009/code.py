
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

# Bass: Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=40, start=2.125, end=2.5),
    # Bar 3: A2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=41, start=2.875, end=3.125),
    pretty_midi.Note(velocity=90, pitch=44, start=3.125, end=3.5),
    # Bar 4: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=37, start=3.875, end=4.125),
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),
    # Bar 5: G2 (seventh) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=43, start=5.125, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # C4
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # F4
])
# Bar 4: Dm7 (D-F-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # C4
])
# Bar 5: C7 (C-E-G-B)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # B4
])
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick_3])

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare, snare_4])

# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)
        drums.notes.append(hihat)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: D4 (62) on beat 1, F#4 (67) on beat 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # F#4
]
# Bar 3: A4 (69) on beat 1
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.625))  # A4
# Bar 4: D4 (62) on beat 1, resolution
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625))  # D4
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
