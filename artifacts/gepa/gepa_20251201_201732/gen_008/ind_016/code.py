
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.375, end=0.75), # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Marcus - Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0), # F2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75), # G#2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5), # Eb2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875), # Eb2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0), # F2
]
bass.notes.extend(bass_notes)

# PIANO: Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # C4
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875), # E4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375), # Ab4

    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # C4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # E4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # B4
]
piano.notes.extend(piano_notes)

# SAX: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (72), Ab (73), Bb (71), F (72)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),   # F4
    pretty_midi.Note(velocity=100, pitch=73, start=1.75, end=2.0),   # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),   # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),   # F4 (end of motif)

    # Repeat motif, slightly varied
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),   # F4
    pretty_midi.Note(velocity=100, pitch=73, start=4.75, end=5.0),   # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),   # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),   # F4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.75)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 2.25)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
