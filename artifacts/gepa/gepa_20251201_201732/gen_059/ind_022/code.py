
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2 (F root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F#2 (b5 chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (F 5th)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0), # E2 (F 3rd)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25), # E4 (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25), # A4 (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25), # C5 (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=2.25), # F5 (Fmaj7)
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875), # A4 (Fmaj7 9th)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # C5 (Fmaj7 3rd)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in F (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375), # G2 (F 5th)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F#2 (b5 chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2 (F root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5), # E2 (F 3rd)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7b5 (B, D, F, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75), # A4 (Bm7b5)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75), # E4 (Bm7b5)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # B4 (Bm7b5)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75), # C5 (Bm7b5)
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375), # A4
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75), # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # A4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in F (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875), # E2 (F 3rd)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2 (F root)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # F#2 (b5 chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0), # G2 (F 5th)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25), # E4 (F7)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25), # A4 (F7)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.25), # C5 (F7)
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=5.25), # F5 (F7)
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif (finish the phrase)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # A4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0), # B4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
