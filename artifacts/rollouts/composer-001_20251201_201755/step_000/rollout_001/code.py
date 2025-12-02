
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.375),  # C3 (octave)
    pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.75), # B2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=80, start=3.75, end=4.125), # C3 (octave)
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625), # F2 (root)
    pretty_midi.Note(velocity=100, pitch=80, start=5.625, end=6.0),  # C3 (octave)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=89, start=1.5, end=1.875),  # E
]
# Bar 3: Bm7 (B, D, F, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=86, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=89, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.625),  # A
])
# Bar 4: E7 (E, G#, B, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=92, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),  # D
])
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F, Bb, C, E (F7sus4) - start it on bar 2, leave it hanging on Bb, come back in bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=2.875),  # C (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.0),    # F (come back)
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=4.25, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=89, start=4.5, end=4.875),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
