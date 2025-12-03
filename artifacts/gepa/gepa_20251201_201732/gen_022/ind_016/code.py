
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (but cut off at bar end)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # C5
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F4
]
# Bar 4: C7 (C, E, G, Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # E5
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, start it, leave it hanging, come back and finish it
# Motif: F4, Bb4, F4, Bb4, C5, F4 (saxophone range: F4 to C5)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),   # F4
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=110, pitch=76, start=2.625, end=3.0),   # Bb4
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.375),   # C5
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),   # F4 (come back)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5s to 3.0s
bar2_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
bar2_snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
bar2_hihat = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend([bar2_kick, bar2_snare] + bar2_hihat)

# Bar 3: 3.0s to 4.5s
bar3_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
bar3_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
bar3_hihat = [
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend([bar3_kick, bar3_snare] + bar3_hihat)

# Bar 4: 4.5s to 6.0s
bar4_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
bar4_snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
bar4_hihat = [
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend([bar4_kick, bar4_snare] + bar4_hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
