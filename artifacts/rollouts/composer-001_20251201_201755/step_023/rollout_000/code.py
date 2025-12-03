
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

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0),  # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # D2 (root)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),  # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=54, start=3.5, end=3.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),  # D2 (root)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.75),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),  # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=52, start=5.0, end=5.25),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F Ab C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),  # Ab4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # C4
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),  # F4
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - Eb4 - D4 (1 bar), then repeat with slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D4
]
sax.notes.extend(sax_notes)

# Drums: bar 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    kick_start = start + 0.0
    kick_end = start + 0.375
    kick2_start = start + 1.125
    kick2_end = start + 1.5
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick2_start, end=kick2_end))
    # Snare on 2 and 4
    snare_start = start + 0.75
    snare_end = start + 0.875
    snare2_start = start + 1.875
    snare2_end = start + 2.0
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare2_start, end=snare2_end))
    # Hi-hat on every eighth
    for i in range(8):
        hihat_start = start + (i * 0.1875)
        hihat_end = hihat_start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
