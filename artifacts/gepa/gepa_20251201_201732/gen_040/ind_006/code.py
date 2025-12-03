
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

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125)
drum_snare2 = pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth
for i in range(0, 4):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=(i+1)*0.375)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
# D2-G2, MIDI 38-43

# Bar 2 (1.5 - 3.0s)
note_d = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)
note_f = pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25)
note_g = pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625)
note_b = pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0)
bass.notes.append(note_d)
bass.notes.append(note_f)
bass.notes.append(note_g)
bass.notes.append(note_b)

# Bar 3 (3.0 - 4.5s)
note_c = pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375)
note_d = pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75)
note_f = pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125)
note_g = pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5)
bass.notes.append(note_c)
bass.notes.append(note_d)
bass.notes.append(note_f)
bass.notes.append(note_g)

# Bar 4 (4.5 - 6.0s)
note_a = pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875)
note_b = pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25)
note_d = pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625)
note_f = pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0)
bass.notes.append(note_a)
bass.notes.append(note_b)
bass.notes.append(note_d)
bass.notes.append(note_f)

# Piano: Open voicings, different chord each bar, resolve on the last

# Bar 2 (1.5 - 3.0s)
# D7sus4: D, G, C, F
note_d_p = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)
note_g_p = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)
note_c_p = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0)
note_f_p = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0)
piano.notes.append(note_d_p)
piano.notes.append(note_g_p)
piano.notes.append(note_c_p)
piano.notes.append(note_f_p)

# Bar 3 (3.0 - 4.5s)
# G7sus4: G, C, F, B
note_g_p2 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)
note_c_p2 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5)
note_f_p2 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5)
note_b_p2 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5)
piano.notes.append(note_g_p2)
piano.notes.append(note_c_p2)
piano.notes.append(note_f_p2)
piano.notes.append(note_b_p2)

# Bar 4 (4.5 - 6.0s)
# C7sus4: C, F, B, E
note_c_p3 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0)
note_f_p3 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0)
note_b_p3 = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)
note_e_p3 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0)
piano.notes.append(note_c_p3)
piano.notes.append(note_f_p3)
piano.notes.append(note_b_p3)
piano.notes.append(note_e_p3)

# Sax: Melody. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (1.5 - 3.0s)
# motif: D (62), F# (66), B (69), D (62)
note_d_sax = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
note_fs_sax = pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25)
note_b_sax = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625)
note_d_sax2 = pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)
sax.notes.append(note_d_sax)
sax.notes.append(note_fs_sax)
sax.notes.append(note_b_sax)
sax.notes.append(note_d_sax2)

# Bar 3 (3.0 - 4.5s)
# leave it hanging
note_rest = pretty_midi.Note(velocity=0, pitch=60, start=3.0, end=3.375)
note_rest2 = pretty_midi.Note(velocity=0, pitch=60, start=3.375, end=3.75)
note_rest3 = pretty_midi.Note(velocity=0, pitch=60, start=3.75, end=4.125)
note_rest4 = pretty_midi.Note(velocity=0, pitch=60, start=4.125, end=4.5)
sax.notes.append(note_rest)
sax.notes.append(note_rest2)
sax.notes.append(note_rest3)
sax.notes.append(note_rest4)

# Bar 4 (4.5 - 6.0s)
# come back and finish it
note_d_sax3 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
note_fs_sax2 = pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25)
note_b_sax2 = pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625)
note_d_sax4 = pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0)
sax.notes.append(note_d_sax3)
sax.notes.append(note_fs_sax2)
sax.notes.append(note_b_sax2)
sax.notes.append(note_d_sax4)

# Drums for bars 2-4
# Kick on 1 and 3
drum_kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drum_kick5 = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drums.notes.append(drum_kick3)
drums.notes.append(drum_kick4)
drums.notes.append(drum_kick5)

# Snare on 2 and 4
drum_snare3 = pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75)
drum_snare4 = pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875)
drum_snare5 = pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=6.0)
drums.notes.append(drum_snare3)
drums.notes.append(drum_snare4)
drums.notes.append(drum_snare5)

# Hi-hat on every eighth for bars 2-4
for i in range(4, 12):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=i*0.375, end=(i+1)*0.375)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
