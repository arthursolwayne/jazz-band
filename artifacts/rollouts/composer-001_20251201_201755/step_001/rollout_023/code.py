
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # E (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E♭)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # E♭ (E♭5)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25), # B4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # E (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: B7 (B D# F# A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=4.5),  # D# (D#5)
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=4.5),  # F# (F#5)
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # A (A5)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75), # D5
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.125), # C5
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # B4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # E (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # F (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # G2 (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: E7 (E G# B D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E (E4)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # G# (G#4)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # D (D5)
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25), # C5
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625), # B4
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # A4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
