
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

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus on walking line, roots and fifths with chromatic approaches
# Fm7: F, C, Ab, D
# Bar 2: F, Eb, C, Ab
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0), # Ab
    # Bar 3: Bb, F, Eb, C
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5), # C
    # Bar 4: Ab, G, F, Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0), # Eb
]
bass.notes.extend(bass_notes)

# Piano: Diane on open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Ab
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Ab
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Dante on one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, G, Eb (bars 2-4)
# Bar 2: F, Ab
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Ab
    # Bar 3: G, Eb (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # Eb
    # Bar 4: F, Ab (come back and finish it)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Ab
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2, hihat, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
