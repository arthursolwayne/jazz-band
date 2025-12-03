
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, Bb, Db), chromatic approach on 1
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F (root)
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25), # Ab (4th)
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # Bb (5th)
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),  # Db (b7)
]

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 Chord: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),   # Eb
]

# Sax: One short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # G (Fm7)
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # Bb (Fm7)
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625), # F (Fm7)
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # B (extension)
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (F, Ab, Bb, Db), chromatic approach on 1
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375), # F (root)
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # Ab (4th)
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125), # Bb (5th)
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),  # Db (b7)
])

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes.extend([
    # Bar 3 Chord: Ab7 (Ab, C, Eb, Gb)
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=4.5),   # Gb
])

# Sax: Continue motif, leave it hanging
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375), # G (Ab7)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # Bb (Ab7)
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125), # F (Ab7)
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # B (extension)
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (F, Ab, Bb, Db), chromatic approach on 1
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # F (root)
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Ab (4th)
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # Bb (5th)
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),  # Db (b7)
])

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes.extend([
    # Bar 4 Chord: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=6.0),   # Ab
])

# Sax: Finish the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875), # G (Bb7)
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # Bb (Bb7)
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625), # F (Bb7)
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # B (extension)
])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
])

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
