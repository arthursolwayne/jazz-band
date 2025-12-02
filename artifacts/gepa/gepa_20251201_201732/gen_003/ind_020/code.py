
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625),  # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # Ab2
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # Eb3
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125),  # D3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),  # Eb3
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625),  # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # Ab2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D5
]
# Bar 3: Gb7 (Gb, Bb, Db, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # Gb4
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # Db5
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # Eb5
])
# Bar 4: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Ab5
])
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 (64), Ab4 (67), F4 (64), leave on Ab4 (67) for the first bar
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    # Repeat the motif with slight variation
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    # Final resolution
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # Ab4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("4_bar_intro.mid")
