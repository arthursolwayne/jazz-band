
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

# ---------------------
# Bar 1 (0.0 - 1.5s)
# ---------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # Snare on 4
    # Hi-hats on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# ---------------------
# Bar 2 (1.5 - 3.0s)
# ---------------------
# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Root: F (48), 5th: C (55), chromatic approaches: E# (56) and D (50)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=55, start=1.5, end=1.875),   # C (5th)
    pretty_midi.Note(velocity=70, pitch=56, start=1.875, end=2.25),  # E#
    pretty_midi.Note(velocity=70, pitch=48, start=2.25, end=2.625),  # F (root)
    pretty_midi.Note(velocity=70, pitch=50, start=2.625, end=3.0),   # D (chromatic approach)
]

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F7sus4 (F, Bb, C, D) -> F7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=3.0), # A (resolve to F7)
]

# Dante on sax: one short motif, make it sing, leave it hanging
# Motif: F (66) -> Eb (64) -> F (66) -> rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # F
    # leave it hanging
]

# ---------------------
# Bar 3 (3.0 - 4.5s)
# ---------------------
# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Root: F (48), 5th: C (55), chromatic approaches: E# (56) and D (50)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=55, start=3.0, end=3.375),   # C (5th)
    pretty_midi.Note(velocity=70, pitch=56, start=3.375, end=3.75),  # E#
    pretty_midi.Note(velocity=70, pitch=48, start=3.75, end=4.125),  # F (root)
    pretty_midi.Note(velocity=70, pitch=50, start=4.125, end=4.5),   # D (chromatic approach)
]

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7sus4 (Bb, D, E, F) -> Bb7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=54, start=3.0, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5), # G (resolve to Bb7)
]

# Dante on sax: continue the motif with variation, leave it hanging again
# Motif: F (66) -> Ab (65) -> Bb (62) -> rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # Bb
    # leave it hanging
]

# ---------------------
# Bar 4 (4.5 - 6.0s)
# ---------------------
# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Root: F (48), 5th: C (55), chromatic approaches: E# (56) and D (50)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=55, start=4.5, end=4.875),   # C (5th)
    pretty_midi.Note(velocity=70, pitch=56, start=4.875, end=5.25),  # E#
    pretty_midi.Note(velocity=70, pitch=48, start=5.25, end=5.625),  # F (root)
    pretty_midi.Note(velocity=70, pitch=50, start=5.625, end=6.0),   # D (chromatic approach)
]

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 4: D7sus4 (D, F#, G, A) -> D7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=6.0),  # F#
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0), # B (resolve to D7)
]

# Dante on sax: finish the motif with a half-step resolution, leave it open
# Motif: F (66) -> Eb (64) -> D (62) -> rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    # leave it open
]

# ---------------------
# Add notes to instruments
# ---------------------
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
