
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - walking bass line (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0), # D2
]
bass.notes.extend(bass_notes)

# Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0), # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0), # A4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0), # C#5
]
piano.notes.extend(piano_notes)

# Dante - saxophone, motif
# Short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0), # F#4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - walking bass line (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5), # D2
]
bass.notes.extend(bass_notes)

# Diane - open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5), # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.5), # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.5), # D5
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.5), # F5
]
piano.notes.extend(piano_notes)

# Dante - saxophone, motif continuation
# Come back and finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5), # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75), # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0), # D4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875), # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0), # Snare
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - walking bass line (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875), # B2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0), # A2
]
bass.notes.extend(bass_notes)

# Diane - open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C E G B)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.0), # C4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.0), # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0), # B4
]
piano.notes.extend(piano_notes)

# Dante - saxophone, motif completion
# Finish the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0), # F#4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375), # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125), # Snare
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
