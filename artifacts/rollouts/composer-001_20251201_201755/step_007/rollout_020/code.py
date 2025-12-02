
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0), # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875), # Ab2
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875), # C2
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875), # D2
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75), # G3
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0), # A3
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5), # G3
    pretty_midi.Note(velocity=110, pitch=57, start=2.5, end=2.75), # F3
    pretty_midi.Note(velocity=110, pitch=59, start=2.75, end=3.0), # G3
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5), # C2
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375), # C2
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375), # Eb2
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # G2
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, imply a question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=59, start=3.0, end=3.25), # G3
    pretty_midi.Note(velocity=110, pitch=61, start=3.25, end=3.5), # A3
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75), # Bb3
    pretty_midi.Note(velocity=110, pitch=59, start=3.75, end=4.0), # G3
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0), # C2
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875), # Bb2
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875), # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875), # Ab2
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, answer the question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.75), # F3
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=5.0), # G3
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25), # A3
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.5), # F3
    pretty_midi.Note(velocity=110, pitch=60, start=5.5, end=5.75), # G3
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0), # A3
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
