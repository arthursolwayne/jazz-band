
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (bar 2, beat 1)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F#2 (beat 2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2 (beat 3)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2 (beat 4)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # G2 (bar 3, beat 1)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),  # B2 (beat 2)
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # D2 (beat 3)
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # G2 (beat 4)
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # A#2 (bar 4, beat 1)
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # B2 (beat 2)
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # D2 (beat 3)
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),  # G2 (beat 4)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.875),  # C#4
    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F#4
    # Bar 4: A7 (A, C#, E, G#)
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # C#4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # E5
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G#4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F#4, G4, D4 (with a slight chromatic approach)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=56, start=1.625, end=1.75),  # E4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=57, start=1.75, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=58, start=1.875, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.125),  # D4
    pretty_midi.Note(velocity=100, pitch=55, start=2.125, end=2.625),  # D4 (rest)
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=56, start=2.75, end=2.875),  # E4
    pretty_midi.Note(velocity=100, pitch=57, start=2.875, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.125),  # G4
    pretty_midi.Note(velocity=100, pitch=55, start=3.125, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=55, start=3.25, end=3.75),  # D4 (rest)
]
sax.notes.extend(sax_notes)

# Drums continue with the same pattern for bars 2-4
for i in range(1, 4):
    start = 1.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),  # Hihat on 1
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),  # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),  # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),  # Hihat on 3
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875),  # Hihat on 4
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),  # Snare on 4
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
