
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
bar_1_start = 0.0
bar_1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_1_start, end=bar_1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_1_start + 1.125, end=bar_1_start + 1.5)
drums.notes.extend([kick1, kick2])

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_1_start + 0.75, end=bar_1_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_1_start + 1.875, end=bar_1_start + 1.875 + 0.375)
drums.notes.extend([snare1, snare2])

# Hihat on every eighth
hihat_notes = [bar_1_start + i * 0.375 for i in range(4)]
for h in hihat_notes:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.125)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
bar_2_start = 1.5
bar_2_end = 3.0

# Bass: D2 (MIDI 38) to G2 (MIDI 43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar_2_start, end=bar_2_start + 0.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=bar_2_start + 0.375, end=bar_2_start + 0.75),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=bar_2_start + 0.75, end=bar_2_start + 1.125),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_2_start + 1.125, end=bar_2_start + 1.5),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_2_start + 1.5, end=bar_2_start + 1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=bar_2_start + 1.875, end=bar_2_start + 2.25),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=bar_2_start + 2.25, end=bar_2_start + 2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_2_start + 2.625, end=bar_2_start + 3.0)   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=bar_2_start, end=bar_2_end)  # D4
note2 = pretty_midi.Note(velocity=100, pitch=67, start=bar_2_start, end=bar_2_end)  # F#4
note3 = pretty_midi.Note(velocity=100, pitch=69, start=bar_2_start, end=bar_2_end)  # A4
note4 = pretty_midi.Note(velocity=100, pitch=64, start=bar_2_start, end=bar_2_end)  # C4
piano.notes.extend([note1, note2, note3, note4])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_2_start, end=bar_2_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_2_start + 1.125, end=bar_2_start + 1.5)
drums.notes.extend([kick1, kick2])

snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_2_start + 0.75, end=bar_2_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_2_start + 1.875, end=bar_2_start + 1.875 + 0.375)
drums.notes.extend([snare1, snare2])

hihat_notes = [bar_2_start + i * 0.375 for i in range(4)]
for h in hihat_notes:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.125)
    drums.notes.append(hihat)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), E4 (64), F#4 (67), D4 (62)
note1 = pretty_midi.Note(velocity=110, pitch=62, start=bar_2_start, end=bar_2_start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=64, start=bar_2_start + 0.375, end=bar_2_start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=bar_2_start + 0.75, end=bar_2_start + 1.125)
note4 = pretty_midi.Note(velocity=110, pitch=62, start=bar_2_start + 2.25, end=bar_2_start + 2.625)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Full quartet (3.0 - 4.5s)
bar_3_start = 3.0
bar_3_end = 4.5

# Bass: D2 (MIDI 38) to G2 (MIDI 43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar_3_start, end=bar_3_start + 0.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=bar_3_start + 0.375, end=bar_3_start + 0.75),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=bar_3_start + 0.75, end=bar_3_start + 1.125),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_3_start + 1.125, end=bar_3_start + 1.5),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_3_start + 1.5, end=bar_3_start + 1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=bar_3_start + 1.875, end=bar_3_start + 2.25),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=bar_3_start + 2.25, end=bar_3_start + 2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_3_start + 2.625, end=bar_3_start + 3.0)   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B D F# A)
note1 = pretty_midi.Note(velocity=100, pitch=69, start=bar_3_start, end=bar_3_end)  # B4
note2 = pretty_midi.Note(velocity=100, pitch=72, start=bar_3_start, end=bar_3_end)  # D5
note3 = pretty_midi.Note(velocity=100, pitch=76, start=bar_3_start, end=bar_3_end)  # F#5
note4 = pretty_midi.Note(velocity=100, pitch=69, start=bar_3_start, end=bar_3_end)  # A4
piano.notes.extend([note1, note2, note3, note4])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_3_start, end=bar_3_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_3_start + 1.125, end=bar_3_start + 1.5)
drums.notes.extend([kick1, kick2])

snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_3_start + 0.75, end=bar_3_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_3_start + 1.875, end=bar_3_start + 1.875 + 0.375)
drums.notes.extend([snare1, snare2])

hihat_notes = [bar_3_start + i * 0.375 for i in range(4)]
for h in hihat_notes:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.125)
    drums.notes.append(hihat)

# Sax: Motif continues with a slight variation
note5 = pretty_midi.Note(velocity=110, pitch=69, start=bar_3_start + 0.375, end=bar_3_start + 0.75)
note6 = pretty_midi.Note(velocity=110, pitch=64, start=bar_3_start + 0.75, end=bar_3_start + 1.125)
note7 = pretty_midi.Note(velocity=110, pitch=62, start=bar_3_start + 1.125, end=bar_3_start + 1.5)
note8 = pretty_midi.Note(velocity=110, pitch=67, start=bar_3_start + 1.5, end=bar_3_start + 1.875)
sax.notes.extend([note5, note6, note7, note8])

# Bar 4: Full quartet (4.5 - 6.0s)
bar_4_start = 4.5
bar_4_end = 6.0

# Bass: D2 (MIDI 38) to G2 (MIDI 43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar_4_start, end=bar_4_start + 0.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=bar_4_start + 0.375, end=bar_4_start + 0.75),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=bar_4_start + 0.75, end=bar_4_start + 1.125),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_4_start + 1.125, end=bar_4_start + 1.5),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_4_start + 1.5, end=bar_4_start + 1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=bar_4_start + 1.875, end=bar_4_start + 2.25),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=bar_4_start + 2.25, end=bar_4_start + 2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_4_start + 2.625, end=bar_4_start + 3.0)   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G B D F)
note1 = pretty_midi.Note(velocity=100, pitch=71, start=bar_4_start, end=bar_4_end)  # G4
note2 = pretty_midi.Note(velocity=100, pitch=76, start=bar_4_start, end=bar_4_end)  # B4
note3 = pretty_midi.Note(velocity=100, pitch=74, start=bar_4_start, end=bar_4_end)  # D5
note4 = pretty_midi.Note(velocity=100, pitch=72, start=bar_4_start, end=bar_4_end)  # F4
piano.notes.extend([note1, note2, note3, note4])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_4_start, end=bar_4_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_4_start + 1.125, end=bar_4_start + 1.5)
drums.notes.extend([kick1, kick2])

snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_4_start + 0.75, end=bar_4_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_4_start + 1.875, end=bar_4_start + 1.875 + 0.375)
drums.notes.extend([snare1, snare2])

hihat_notes = [bar_4_start + i * 0.375 for i in range(4)]
for h in hihat_notes:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.125)
    drums.notes.append(hihat)

# Sax: Complete the motif and end it
note9 = pretty_midi.Note(velocity=110, pitch=62, start=bar_4_start + 0.375, end=bar_4_start + 0.75)
note10 = pretty_midi.Note(velocity=110, pitch=64, start=bar_4_start + 0.75, end=bar_4_start + 1.125)
note11 = pretty_midi.Note(velocity=110, pitch=67, start=bar_4_start + 1.125, end=bar_4_start + 1.5)
note12 = pretty_midi.Note(velocity=110, pitch=62, start=bar_4_start + 1.5, end=bar_4_start + 1.875)
note13 = pretty_midi.Note(velocity=110, pitch=64, start=bar_4_start + 1.875, end=bar_4_start + 2.25)
note14 = pretty_midi.Note(velocity=110, pitch=67, start=bar_4_start + 2.25, end=bar_4_start + 2.625)
note15 = pretty_midi.Note(velocity=110, pitch=62, start=bar_4_start + 2.625, end=bar_4_start + 3.0)
sax.notes.extend([note9, note10, note11, note12, note13, note14, note15])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
