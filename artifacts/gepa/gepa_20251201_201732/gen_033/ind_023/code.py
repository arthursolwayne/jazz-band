
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line in Fm, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875), # F (root)
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),  # Bb (chromatic approach)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # F (root)
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # Bb (chromatic approach)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875), # F (root)
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625), # C (fifth)
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),  # Bb (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane on piano (open voicings, different chord each bar, resolve on the last)
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # Eb

    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # Db
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375), # Ab

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C
]
piano.notes.extend(piano_notes)

# Dante on sax (short motif, make it sing)
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75), # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # A

    # Bar 3: Echo/variation
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # E

    # Bar 4: Resolution
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
