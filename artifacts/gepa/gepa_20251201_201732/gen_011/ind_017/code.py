
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone enters
# Bass: D2 (MIDI 38) -> F#2 (MIDI 41) -> G2 (MIDI 43) -> A2 (MIDI 45)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F#2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # A2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7sus4 (D, G, C#, F#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # D5

    # Bar 3: G7#9 (G, B, D, F#, A#)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # A#4

    # Bar 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # C#4
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),   # E4
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),   # G4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (62), F#4 (66), B4 (71), rest, D4 (62), F#4 (66), B4 (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),   # D4 on 1
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),   # F#4 on 2
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),   # B4 on 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.875),# D4 on 1
    pretty_midi.Note(velocity=110, pitch=66, start=2.875, end=3.0),  # F#4 on 2
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25)    # B4 on 3
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2: Kick on 1, Snare on 2, Kick on 3, Snare on 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
